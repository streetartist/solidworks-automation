# AddComment Method (ICommentFolder)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~AddComment`

Adds a comment to this folder.
Adds a comment to this folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddComment( _
   ByVal Text As System.String _
) As Comment
```

```

Dim instance As ICommentFolder
Dim Text As System.String
Dim value As Comment
 
value = instance.AddComment(Text)
```

```

Comment AddComment( 
   System.string Text
)
```

```

Comment^ AddComment( 
   System.String^ Text
) 
```

#### Parameters

*Text*
:   Comment to add to this folder

#### Return Value

Pointer to the [IComment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.md) object

Remarks

To see this comment, use [IFeatureManager::UpdateFeatureTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~UpdateFeatureTree.md) to rebuild the FeatureManager design tree.

Example

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)  
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)  
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommentFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.md)  
[ICommentFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder_members.md)  
[IComment::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Delete.md)  
[IFeature::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddComment.md)  
[IModelDocExtension::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddComment.md)
