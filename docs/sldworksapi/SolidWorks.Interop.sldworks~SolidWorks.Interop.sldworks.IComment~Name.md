# Name Property (IComment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Name`

Gets or sets the name of the comment as it appears in the FeatureManager design tree.
Gets or sets the name of the comment as it appears in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Name As System.String
```

```

Dim instance As IComment
Dim value As System.String
 
instance.Name = value
 
value = instance.Name
```

```

System.string Name {get; set;}
```

```

property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the comment as it appears in the FeatureManager design tree

Remarks

You cannot set this property if the comment is owned by a feature because the name of the comment always matches the name of the feature that owns it. To determine if a comment is owned by a feature, use [IComment::FeatureOwner](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~FeatureOwner.md).

You must rebuild the FeatureManager design tree after setting the name of a comment. Use [IFeatureManager::UpdateFeatureTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~UpdateFeatureTree.md) to perform this action.

Example

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)  
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)  
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.md)  
[IComment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment_members.md)
