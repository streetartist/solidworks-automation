# Symmetric Property (ILocalCircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Symmetric`

Gets or sets whether Direction 2 properties are symmetric with those of Direction 1 of this bidirectional circular component pattern feature.
Gets or sets whether Direction 2 properties are symmetric with those of Direction 1 of this bidirectional circular component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Symmetric As System.Boolean
```

```

Dim instance As ILocalCircularPatternFeatureData
Dim value As System.Boolean
 
instance.Symmetric = value
 
value = instance.Symmetric
```

```

System.bool Symmetric {get; set;}
```

```

property System.bool Symmetric {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if Direction 2 properties mirror Direction 1 properties, false if not

Remarks

This property is only available when [ILocalCircularPatternFeatureData::Direction2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Direction2.md) is true.

If this property is set to false, then you must specify:

- [ILocalCircularPatternFeatureData::EqualSpacing2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing2.md)
- [ILocalCircularPatternFeatureData::TotalInstances2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances2.md)

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)  
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.md)
