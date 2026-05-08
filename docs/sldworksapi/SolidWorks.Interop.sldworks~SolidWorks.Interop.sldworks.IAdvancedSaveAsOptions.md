# IAdvancedSaveAsOptions Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions`

Allows access to all File &gt; Save As options when saving a SOLIDWORKS Part, Assembly, or Drawing.
Allows access to all **File > Save As** options when saving a SOLIDWORKS Part, Assembly, or Drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IAdvancedSaveAsOptions 
```

```

Dim instance As IAdvancedSaveAsOptions
```

```

public interface IAdvancedSaveAsOptions 
```

```

public interface class IAdvancedSaveAsOptions 
```

Example

'VBA

'This example shows how to save a drawing with advanced options.  
'--------------------------------------------------------------  
' Preconditions:  
' 1. Open:  
'    *public\_documents***\samples\tutorial\advdrawings\foodprocessor.slddrw**  
' 2. Open the Immediate window.  
'  
' Postconditions:  
' 1. Inspect the Immediate window for the list of reference components,  
'    before and after name modifications to the drawing and its template.  
' 2. Inspect the DrwSavedFolder and Ref sub-folders. In those  
'     directories, the names of top-level documents are changed to "SamplePart.\*".  
'     The reference component names are changed to include a "Prff\_" prefix and  
'     a "\_Suff" suffix.  
'  
' NOTE: Because the drawing and template are used elsewhere,  
' do not save changes.  
'--------------------------------------------------------------

Dim swApp As SldWorks.SldWorks  
Dim swModel As ModelDoc2  
Dim ModelExt As ModelDocExtension

Dim AdvOptData As AdvancedSaveAsOptions  
Dim aFileName As String  
Dim OrFileName As String  
Dim Opt As Long  
Dim Error As Long  
Dim Warning As Long  
Dim Status As Boolean  
Dim i As Long  
Dim k As Long

Const Suff As String = "\_Suff"  
Const Prff As String = "Prff\_"  
Option Explicit

Sub main()

    Dim DrwExtArr As Variant  
    DrwExtArr = Array(".slddrw", ".drwdot")  
     
    Set swApp = Application.SldWorks  
    Set swModel = swApp.ActiveDoc  
    Set ModelExt = swModel.Extension  
     
    OrFileName = Left(swModel.GetPathName(), InStrRev(swModel.GetPathName(), "\"))  
    Debug.Print OrFileName  
     
    Dim IDList As Variant  
    Dim fileNameList As Variant  
    Dim pathNameList As Variant  
     
     If Dir(OrFileName & "DrwSavedFolder", vbDirectory) = "" Then  
            MkDir (OrFileName & "DrwSavedFolder")  
            MkDir (OrFileName & "Ref")  
        End If  
     
     
    For i = 0 To UBound(DrwExtArr)  
         
        aFileName = OrFileName & "DrwSavedFolder\SamplePart" & DrwExtArr(i)  
        Debug.Print aFileName  
         
        Set AdvOptData = ModelExt.**GetAdvancedSaveAsOptions**((1 + 2 + 4))  
     
        AdvOptData.**SaveAllAsCopy** = True

        'Uncomment the line below to save model and references as SOLIDWORKS 2020

        'AdvOptData.**SaveAsPreviousVersion** = 13000

        
        AdvOptData.**GetItemsNameAndPath** IDList, fileNameList, pathNameList  
         
        PrintList fileNameList, pathNameList  
         
        AdvOptData.**SetPrefixSuffixToAll** Prff, Suff  
         
        AdvOptData.**GetItemsNameAndPath** IDList, fileNameList, pathNameList  
         
        For k = 0 To UBound(IDList)  
     
            If k = 0 Then ' For setting root folder and root file name  
                pathNameList(k) = OrFileName & "DrwSavedFolder"  
                fileNameList(k) = "SamplePart" & DrwExtArr(i)  
            Else  
                pathNameList(k) = OrFileName & "Ref"  
            End If  
     
        Next  
         
        Error = AdvOptData.**ModifyItemsNameAndPath**(IDList, fileNameList, pathNameList)  
         
        Debug.Print "Modify Paths Status : " & Error  
        Debug.Print " "  
        AdvOptData.**GetItemsNameAndPath** IDList, fileNameList, pathNameList  
     
        PrintList fileNameList, pathNameList  
       
        SaveFunctionCall (DrwExtArr(i))  
         
        Debug.Print " "  
     
    Next  
     
    Debug.Print "Total Count " & i

End Sub

Sub SaveFunctionCall(Typ As String)

    Opt = (1 + 2)  
    Debug.Print aFileName  
    Status = ModelExt.**SaveAs3**(aFileName, 0, Opt, Nothing, AdvOptData, Error, Warning)  
     
    Debug.Print "Save Status for Type " & Typ & " is : " & Status & " " & Error & " " & Warning

End Sub

Sub PrintList(sList As Variant, sList2 As Variant)

    Dim j As Long  
     
    For j = 0 To UBound(sList)  
         
        Debug.Print sList(j) & " \*\*>>\*\* " & sList2(j)  
         
    Next  
     
    Debug.Print "Total Count in the List is : " & j

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
