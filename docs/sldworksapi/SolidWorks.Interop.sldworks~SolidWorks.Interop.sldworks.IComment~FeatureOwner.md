# FeatureOwner Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~FeatureOwner`

Gets the feature that owns this comment.
Gets the feature that owns this comment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property FeatureOwner As Feature
```

```

Dim instance As IComment
Dim value As Feature
 
value = instance.FeatureOwner
```

```

Feature FeatureOwner {get;}
```

```

property Feature^ FeatureOwner {
   Feature^ get();
}
```

#### Property Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object that owns this comment

Remarks

If the comment is not owned by a feature, then NULL is returned.

Because you cannot set the name of comment owned by a feature, use this property before using [IComment::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Name.md) to determine if the comment is owned by a feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.md)  
[IComment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment_members.md)
