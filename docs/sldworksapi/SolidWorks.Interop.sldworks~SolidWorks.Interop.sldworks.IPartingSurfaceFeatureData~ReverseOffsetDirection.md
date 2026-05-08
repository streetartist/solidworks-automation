# ReverseOffsetDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~ReverseOffsetDirection`

Gets or sets whether to reverse the direction of this parting surface feature.
Gets or sets whether to reverse the direction of this parting surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseOffsetDirection As System.Boolean
```

```

Dim instance As IPartingSurfaceFeatureData
Dim value As System.Boolean
 
instance.ReverseOffsetDirection = value
 
value = instance.ReverseOffsetDirection
```

```

System.bool ReverseOffsetDirection {get; set;}
```

```

property System.bool ReverseOffsetDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the direction, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.md)  
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.md)
