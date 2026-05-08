# UseAngle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~UseAngle`

Gets or sets whether an angle is used for specifying the dimensions of the polygonal profile for this gusset feature.
Gets or sets whether an angle is used for specifying the dimensions of the polygonal profile for this gusset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseAngle As System.Boolean
```

```

Dim instance As IGussetFeatureData
Dim value As System.Boolean
 
instance.UseAngle = value
 
value = instance.UseAngle
```

```

System.bool UseAngle {get; set;}
```

```

property System.bool UseAngle {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if an angle is used, false if not

Remarks

[IGussetFeatureData::ProfileType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileType.md) must be set to swGussetProfilePolygon.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.md)  
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.md)
