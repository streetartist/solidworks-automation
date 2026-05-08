# GetPartitionStream Method (ISwDMConfiguration2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~GetPartitionStream`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~GetPartitionStream.html) on this topic. |
| GetPartitionStream Method (ISwDMConfiguration2) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2.md) : GetPartitionStream Method (ISwDMConfiguration2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*fileName*
:   Filename to which to write the Parasolid partition and body information (see Remarks)

Gets the Parasolid partition stream that has the body partition information and writes it the specified file. Supports part documents only.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetPartitionStream( _    ByVal fileName As System.String _ ) As SwDmBodyError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration2 Dim fileName As System.String Dim value As SwDmBodyError   value = instance.GetPartitionStream(fileName) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmBodyError GetPartitionStream(     System.string fileName ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmBodyError GetPartitionStream(  &   System.String^ fileName ) ``` | |

#### Parameters

*fileName*
:   Filename to which to write the Parasolid partition and body information (see Remarks)

#### Return Value

Success or error code as defined by [SwDmBodyError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmBodyError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration2::GetPartitionStream](swdocumentmgr~SwDMConfiguration2~GetPartitionStream.md).

# Example

[Write Parasolid Partition Stream to File (C#)](Write_Parasolid_Partition_Stream_to_File_Example_CSharp.htm)
  
[Write Parasolid Partition Stream to File (VB.NET)](Write_Parasolid_Partition_Stream_to_File_Example_VBNET.htm)
  
[Write Parasolid Partition Stream to File (C++)](Write_Parasolid_Partition_Stream_to_File_Example_CPlusPlus_COM.htm)

# Remarks

This method only supports part documents saved in SOLIDWORKS 2004 and later. Use [ISwDMConfiguration::GetBody](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBody.md) for part dcouments saved in SOLIDWORKS 2003 and earlier and assembly documents saved in any version of SOLIDWORKS.

To get the version of a part document, use [ISwDMDocument::GetVersion](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.md).

Before using this method, call [ISwDMConfiguration2::PartitionStreamName](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~PartitionStreamName.md) to get fileName. Valid filename extensions are \*.xmp\_bin for NTFS and \*.p\_b for FAT.

|  |  |
| --- | --- |
| **If fileName...** | **Then...** |
| Does not exit | This method creates the file and writes the Parasolid partition and body information to that file |
| Exists | Writes the Parasolid partition and body information to that file, overwriting any data in that file |

# See Also

#### 

[ISwDMConfiguration2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2.md)
  
[ISwDMConfiguration2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 SP1
