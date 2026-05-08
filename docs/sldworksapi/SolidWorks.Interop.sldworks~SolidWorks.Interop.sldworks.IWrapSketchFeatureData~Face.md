# Face Property (IWrapSketchFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData~Face`

Gets where this face was applied for this wrap feature or sets the face where to apply this wrap feature.
Gets where this face was applied for this wrap feature or sets the face where to apply this wrap feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Face As Face2
```

```

Dim instance As IWrapSketchFeatureData
Dim value As Face2
 
instance.Face = value
 
value = instance.Face
```

```

Face2 Face {get; set;}
```

```

property Face2^ Face {
   Face2^ get();
   void set (    Face2^ value);
}
```

#### Property Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Change Wrap Feature Face (C#)](Change_Wrap_Feature_Face_Example_CSharp.htm)  
[Change Wrap Feature Face (VB.NET)](Change_Wrap_Feature_Face_Example_VBNET.htm)  
[Change Wrap Feature Face (VBA)](Change_Wrap_Feature_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWrapSketchFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.md)  
[IWrapSketchFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData_members.md)
