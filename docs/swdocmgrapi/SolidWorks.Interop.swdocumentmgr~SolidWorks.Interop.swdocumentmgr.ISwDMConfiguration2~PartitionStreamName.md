# PartitionStreamName Property (ISwDMConfiguration2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~PartitionStreamName`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~PartitionStreamName.html) on this topic. |
| PartitionStreamName Property (ISwDMConfiguration2) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2.md) : PartitionStreamName Property (ISwDMConfiguration2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the name of the Parasolid body partition stream.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property PartitionStreamName As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration2 Dim value As System.String   value = instance.PartitionStreamName ``` | |

| C# |  |
| --- | --- |
| ``` System.string PartitionStreamName {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.String^ PartitionStreamName {    System.String^ get(); } ``` | |

#### Property Value

Name of the stream; valid filename extensions are \*.xmp\_bin for NTFS and \*.p\_b for FAT

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration2::PartitionStreamName](swdocumentmgr~SwDMConfiguration2~PartitionStreamName.md).

# Remarks

Call this method before calling [ISwDMConfiguration2::GetPartitionStream](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~GetPartitionStream.md).

# See Also

#### 

[ISwDMConfiguration2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2.md)
  
[ISwDMConfiguration2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 SP1
