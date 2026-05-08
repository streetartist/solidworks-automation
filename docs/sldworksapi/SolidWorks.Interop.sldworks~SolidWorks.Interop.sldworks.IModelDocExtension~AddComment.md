# AddComment Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddComment`

Adds a comment to this document's Comment Folder.
Adds a comment to this document's Comment Folder.

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

Dim instance As IModelDocExtension
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
:   Comment to add to the document's Comment folder

#### Return Value

[Comment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.md) folder

Remarks

A comment is added to the document's Comment folder, and the comment is associated with the preselected item when this method is run.  

For example:

|  |  |
| --- | --- |
| **If...** | **Then the comment is...** |
| A feature is preselected | Associated with the feature (equivalent to running the [IFeature::AddComment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddComment.md) on the selected feature) |
| The Comment folder is preselected | Not associated with any feature, but is added to the Comment folder (equivalent to running the [ICommentFolder::AddComment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~AddComment.md) method) |

Although it might appear that ModelDocExtension::AddComment duplicates IFeature::AddComment and ICommentFolder::AddComment, IModelDocExtension::AddComment is used when recording macros, so it is different. IModelDocExtension::AddComment shares code with the user interface, so it should behave identical to the user interface.

IModelDocExtension::AddComment rebuilds the FeatureManager design tree automatically, which can be a time-consuming operation if the FeatureManager design tree gets large. Take this into consideration before using it.

Example

[Add Comment to Assembly Component (VBA)](Add_Comment_to_Assembly_Component_Example_VB.htm)  
[Add Comment to Assembly Component (VB.NET)](Add_Comment_to_Assembly_Component_Example_VBNET.htm)  
[Add Comment to Assembly Component (C#)](Add_Comment_to_Assembly_Component_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IComment::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Delete.md)
