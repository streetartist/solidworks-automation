# GetBody Method (ISwDMConfiguration)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBody`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBody.html) on this topic. |
| GetBody Method (ISwDMConfiguration) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md) : GetBody Method (ISwDMConfiguration) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*index*
:   Index number indicating the body to get

*fileName*
:   Full path and filename in which to get the body

Gets the body at the specified index in the specified Parasolid binary file (filename extension .x\_b).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetBody( _    ByVal index As System.Integer, _    ByVal fileName As System.String _ ) As SwDmBodyError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration Dim index As System.Integer Dim fileName As System.String Dim value As SwDmBodyError   value = instance.GetBody(index, fileName) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmBodyError GetBody(     System.int index,    System.string fileName ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmBodyError GetBody(  &   System.int index, &   System.String^ fileName ) ``` | |

#### Parameters

*index*
:   Index number indicating the body to get

*fileName*
:   Full path and filename in which to get the body

#### Return Value

Success or error code as defined by [SwDmBodyError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmBodyError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration::GetBody](swdocumentmgr~SwDMConfiguration~GetBody.md).

# Example

[Write Parasolid Partition Stream to File (C#)](Write_Parasolid_Partition_Stream_to_File_Example_CSharp.htm)
  
[Write Parasolid Partition Stream to File (VB.NET)](Write_Parasolid_Partition_Stream_to_File_Example_VBNET.htm)

# Remarks

This method supports:

- part and assembly documents saved in SOLIDWORKS 2003 and earlier.
- only assembly documents saved in SOLIDWORKS 2004 and later. Use [ISwDMConfiguration2::GetPartitionStream](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~GetPartitionStream.md) for part documents saved in SOLIDWORKS 2004 and later.

To get the version of a document, use [ISwDMDocument::GetVersion](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.md).

To find out the number of solid bodies in this Parasolid binary file, call [ISwDMConfiguration::GetBodiesCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBodiesCount.md) before calling this method.

# See Also

#### 

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md)
  
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.md)
  
[ISwDMConfiguration3::GetImportedBodiesCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBodiesCount.md)
  
[ISwDMConfiguration3::GetImportedBody Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBody.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
