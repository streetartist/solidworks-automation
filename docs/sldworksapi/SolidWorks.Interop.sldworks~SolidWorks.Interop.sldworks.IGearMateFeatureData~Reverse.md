# Reverse Property (IGearMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData~Reverse`

Gets or sets whether to change the direction of rotation of the gears relative to one another in this gear mate.
Gets or sets whether to change the direction of rotation of the gears relative to one another in this gear mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Reverse As System.Boolean
```

```

Dim instance As IGearMateFeatureData
Dim value As System.Boolean
 
instance.Reverse = value
 
value = instance.Reverse
```

```

System.bool Reverse {get; set;}
```

```

property System.bool Reverse {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the direction of rotation, false to not

Example

See the [IGearMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGearMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.md)  
[IGearMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData_members.md)
