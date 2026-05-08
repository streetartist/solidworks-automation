# InsertBendNotes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBendNotes`

Inserts bend notes for the specified flat-pattern feature of this sheet metal part.
Inserts bend notes for the specified flat-pattern feature of this sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBendNotes( _
   ByVal FlatPatternFeature As System.Object _
) As System.Object
```

```

Dim instance As IPartDoc
Dim FlatPatternFeature As System.Object
Dim value As System.Object
 
value = instance.InsertBendNotes(FlatPatternFeature)
```

```

System.object InsertBendNotes( 
   System.object FlatPatternFeature
)
```

```

System.Object^ InsertBendNotes( 
   System.Object^ FlatPatternFeature
) 
```

#### Parameters

*FlatPatternFeature*
:   [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

#### Return Value

Array of [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)s

Example

'VBA

' 1. Open a sheet metal part with a **Flat-Pattern1** feature.  
' 2. Run the macro.  
' 3. Inspect the Immediate window for the list of inserted bend notes.

Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim myFlatPattern As SldWorks.Feature  
Dim myBendNotes As Variant  
Dim myAnno As SldWorks.Note  
Dim boolstatus As Boolean  
Dim i As Long  
Option Explicit

Sub main()

    Set swApp = Application.SldWorks  
    Set Part = swApp.ActiveDoc  
    boolstatus = Part.Extension.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)  
     
    Set myFlatPattern = Part.SelectionManager.GetSelectedObject6(1, -1)  
    If Not myFlatPattern Is Nothing Then  
        myBendNotes = Part.**InsertBendNotes**(myFlatPattern)  
        For i = 0 To UBound(myBendNotes)  
            Set myAnno = myBendNotes(i)  
            Debug.Print myAnno.GetName  
        Next i  
    End If

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
