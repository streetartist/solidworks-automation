# FlipProfileDistanceParameters Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~FlipProfileDistanceParameters`

Gets or sets whether the Profile Distance 1 and Profile Distance 2 parameters are flipped for this gusset feature.
Gets or sets whether the Profile Distance 1 and Profile Distance 2 parameters are flipped for this gusset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlipProfileDistanceParameters As System.Boolean
```

```

Dim instance As IGussetFeatureData
Dim value As System.Boolean
 
instance.FlipProfileDistanceParameters = value
 
value = instance.FlipProfileDistanceParameters
```

```

System.bool FlipProfileDistanceParameters {get; set;}
```

```

property System.bool FlipProfileDistanceParameters {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip Profile Distance 1 and Profile Distance 2 parameters, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.md)  
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.md)
