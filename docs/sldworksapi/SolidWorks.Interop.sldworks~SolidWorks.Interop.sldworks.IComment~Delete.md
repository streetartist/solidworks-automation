# Delete Method (IComment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Delete`

Deletes a comment.
Deletes a comment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Delete() As System.Boolean
```

```

Dim instance As IComment
Dim value As System.Boolean
 
value = instance.Delete()
```

```

System.bool Delete()
```

```

System.bool Delete(); 
```

#### Return Value

True if the comment is deleted, false if not

Remarks

The comment to delete must not be selected in the FeatureManager design tree. Use [IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.md) to ensure that the comment is not currently selected.

You must rebuild the FeatureManager design tree after deleting the comment. Use [IFeatureManager::UpdateFeatureTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~UpdateFeatureTree.md) to perform this action.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.md)  
[IComment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment_members.md)  
[ICommentFolder::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~AddComment.md)  
[IFeature::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddComment.md)  
[IModelDocExtension::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddComment.md)
