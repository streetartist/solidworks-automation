# TargetBody Property (ICoreFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~TargetBody`

Gets or sets the target body for this core feature.
Gets or sets the target body for this core feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TargetBody As Body2
```

```

Dim instance As ICoreFeatureData
Dim value As Body2
 
instance.TargetBody = value
 
value = instance.TargetBody
```

```

Body2 TargetBody {get; set;}
```

```

property Body2^ TargetBody {
   Body2^ get();
   void set (    Body2^ value);
}
```

#### Property Value

Pointer to the [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) from which this core will be extracted

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.md)  
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.md)
