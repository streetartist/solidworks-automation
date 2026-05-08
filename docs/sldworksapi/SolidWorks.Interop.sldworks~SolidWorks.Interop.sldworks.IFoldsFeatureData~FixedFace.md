# FixedFace Property (IFoldsFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~FixedFace`

Gets or sets the fixed face of this fold feature.
Gets or sets the fixed face of this fold feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FixedFace As System.Object
```

```

Dim instance As IFoldsFeatureData
Dim value As System.Object
 
instance.FixedFace = value
 
value = instance.FixedFace
```

```

System.object FixedFace {get; set;}
```

```

property System.Object^ FixedFace {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Fixed [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Insert and Access Fold Feature (C#)](Insert_and_Access_Fold_Feature_Example_CSharp.htm)  
[Insert and Access Fold Feature (VB.NET)](Insert_and_Access_Fold_Feature_Example_VBNET.htm)  
[Insert and Access Fold Feature (VBA)](Insert_and_Access_Fold_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFoldsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData.md)  
[IFoldsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData_members.md)
