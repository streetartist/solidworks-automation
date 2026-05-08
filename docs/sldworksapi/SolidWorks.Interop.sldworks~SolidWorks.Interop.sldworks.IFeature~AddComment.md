# AddComment Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddComment`

Adds a comment to this feature.
Adds a comment to this feature.

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

Dim instance As IFeature
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
:   Comment to add to this feature

#### Return Value

Pointer to the [IComment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.md) object

Remarks

The comment is added in the [Comment folder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.md), but the comment is associated with this feature.  If your pointer is on the feature in the FeatureManager design tree, then the comment is displayed as a ToolTip.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IComment::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Delete.md)  
[IModelDocExtension::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddComment.md)  
[ICommentFolder::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~AddComment.md)
