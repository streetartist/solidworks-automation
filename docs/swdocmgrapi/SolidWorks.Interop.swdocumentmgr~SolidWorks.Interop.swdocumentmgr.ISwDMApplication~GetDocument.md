# GetDocument Method (ISwDMApplication)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetDocument`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetDocument.html) on this topic. |
| GetDocument Method (ISwDMApplication) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.md) : GetDocument Method (ISwDMApplication) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FullPathName*
:   Full path and filename of the document to get

*docType*
:   Type of document as defined by [SwDmDocumentType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentType.md)

*allowReadOnly*
:   True to open the document as read-only, false as read-write

*result*
:   Error as defined by [SwDmDocumentOpenError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError.md)

Gets the specified document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetDocument( _    ByVal FullPathName As System.String, _    ByVal docType As SwDmDocumentType, _    ByVal allowReadOnly As System.Boolean, _    ByRef result As SwDmDocumentOpenError _ ) As SwDMDocument ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMApplication Dim FullPathName As System.String Dim docType As SwDmDocumentType Dim allowReadOnly As System.Boolean Dim result As SwDmDocumentOpenError Dim value As SwDMDocument   value = instance.GetDocument(FullPathName, docType, allowReadOnly, result) ``` | |

| C# |  |
| --- | --- |
| ``` SwDMDocument GetDocument(     System.string FullPathName,    SwDmDocumentType docType,    System.bool allowReadOnly,    out SwDmDocumentOpenError result ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDMDocument^ GetDocument(  &   System.String^ FullPathName, &   SwDmDocumentType docType, &   System.bool allowReadOnly, &   [Out] SwDmDocumentOpenError result ) ``` | |

#### Parameters

*FullPathName*
:   Full path and filename of the document to get

*docType*
:   Type of document as defined by [SwDmDocumentType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentType.md)

*allowReadOnly*
:   True to open the document as read-only, false as read-write

*result*
:   Error as defined by [SwDmDocumentOpenError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError.md)

#### Return Value

Pointer to an [ISwDMDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) object

# Visual Basic for Applications (VBA) Syntax

See [SwDMApplication::GetDocument](swdocumentmgr~SwDMApplication~GetDocument.md).

# Example

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
  
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
  
[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
  
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)
  
[Write Parasolid Partition Stream to File (C++)](Write_Parasolid_Partition_Stream_to_File_Example_CPlusPlus_COM.htm)
  
[Open and Close Document (C++)](Open_and_Close_Document_Example_CPlusCPlus_COM.htm)
  
[Get Drawing Sheets' Properties (C#)](Get_Drawing_Sheets_Properties_Example_CSharp.htm)
  
[Get Drawing Sheets' Properties (VB.NET)](Get_Drawing_Sheets_Properties_Example_vbnet.htm)
  
[Replace Component (C#)](Replace_Component_Example_CSharp.htm)
  
[Replace Component (VB.NET)](Replace_Component_Example_VBNET.htm)
  
[Get Whether Component Is Envelope and Excluded from BOM (C#)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_CSharp.htm)
  
[Get Whether Component Is Envelope and Excluded from BOM (VB.NET)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_VBNET.htm)

# Remarks

If the document is currently open as read-write, then this method fails and returns NULL.

Use [ISwDMApplication2::GetDocument2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2~GetDocument2.md) to get a document using an IStream or IStorage storage.

# See Also

#### 

[ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.md)
  
[ISwDMApplication Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
