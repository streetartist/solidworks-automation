# GetDisplayTitleName Method (ISwDMDocument25)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument25~GetDisplayTitleName`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument25~GetDisplayTitleName.html) on this topic. |
| GetDisplayTitleName Method (ISwDMDocument25) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument25 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument25.md) : GetDisplayTitleName Method (ISwDMDocument25) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the display title name of this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetDisplayTitleName() As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument25 Dim value As System.String   value = instance.GetDisplayTitleName() ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetDisplayTitleName() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetDisplayTitleName(); ``` | |

#### Return Value

Display title name

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument25::GetDisplayTitleName](swdocumentmgr~SwDMDocument25~GetDisplayTitleName.md).

# Example

'VB.NET

'----------------------------------------------------------------------------  
' Preconditions:  
  
' 1. Read the SOLIDWORKS Document Manager API **Getting Started**  
'    topic and ensure that the required DLLs are registered.  
'  
' 2. Copy and paste this code into a VB.NET console application  
'    in Microsoft Visual Studio.  
'  
' 3. Add the **SolidWorks.Interop.swdocumentmgr.dll** reference to the project:  
'    a. Right-click the solution in Solution Explorer.  
'    b. Click **Add Reference**.  
'    c. Click **Browse**.  
'    d. Click:  
'   *install\_dir***\api\redist\SolidWorks.Interop.swdocumentmgr.dll**'    e. Click **Add.**'    f. Click **Close.**'  
' 4. Substitute *model\_path\_and\_filename*with the path and filename of the model to open.  
'  
' 5. Substitute *your\_license\_key* with your SOLIDWORKS Document  
'    Manager license key.  
'  
' 6. Open the Immediate window.  
'  
' Postconditions: Inspect the Immediate window.  
'  
' **NOTE**: If the model is used elsewhere, do not save changes.  
'--------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swdocumentmgr

Imports SolidWorks.Interop.swconst

Imports System.Runtime.InteropServices

Imports System

Partial Class SolidWorksMacro

    Sub main()

        Dim swClassFact As SwDMClassFactory

        Dim swDocMgr As SwDMApplication

        Dim swDoc As SwDMDocument25

        Dim sLicenseKey As String

        sLicenseKey = "your\_license\_key"

        Dim sDocFileName As String

        sDocFileName = "model\_path\_and\_filename"

        Dim nDocType As Integer

        nDocType = SwDmDocumentType.swDmDocumentPart

        swClassFact = New SwDMClassFactory

        swDocMgr = swClassFact.GetApplication(sLicenseKey)

        Dim retval As SwDmDocumentOpenError

        swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, False, retval)

        Debug.Print("File = " + swDoc.FullName)

        Debug.Print("DisplayTitleName = " + swDoc.**GetDisplayTitleName**)

        swDoc.CloseDoc

    End Sub

    ''' <summary>

    ''' The SldWorks swApp variable is pre-assigned for you.

    ''' </summary>

    Public swApp As SldWorks

End Class

# Example

[Get Display Title Name (C#)](Get_Display_Title_Name_Example_CSharp.htm)

# See Also

#### 

[ISwDMDocument25 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument25.md)
  
[ISwDMDocument25 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument25_members.md)

# Availability

SOLIDWORKS Document Manager API 2020 SP04
