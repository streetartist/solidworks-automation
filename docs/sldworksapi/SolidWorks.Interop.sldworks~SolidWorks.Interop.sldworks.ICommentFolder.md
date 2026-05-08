# ICommentFolder Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder`

Allows access to the Comment folder in the FeatureManager design tree.
Allows access to the Comment folder in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICommentFolder 
```

```

Dim instance As ICommentFolder
```

```

public interface ICommentFolder 
```

```

public interface class ICommentFolder 
```

Remarks

|  |  |
| --- | --- |
| **To...** | **Then use...** |
| Get comments | - [ICommentFolder::GetComments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~GetComments.md), which returns an array of comments - [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md), which returns a single comment |
| Add comments | - [ICommentFolder::AddComment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~AddComment.md) - [IFeature::AddComment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddComment.md) - [IModelDocExtension::AddComment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddComment.md) |

Example

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)  
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)  
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommentFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IComment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.md)
