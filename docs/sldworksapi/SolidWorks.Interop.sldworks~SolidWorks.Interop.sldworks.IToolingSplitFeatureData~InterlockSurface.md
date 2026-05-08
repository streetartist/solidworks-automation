# InterlockSurface Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~InterlockSurface`

Gets or sets whether to create an interlock surface for this tooling split feature.
Gets or sets whether to create an interlock surface for this tooling split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InterlockSurface As System.Boolean
```

```

Dim instance As IToolingSplitFeatureData
Dim value As System.Boolean
 
instance.InterlockSurface = value
 
value = instance.InterlockSurface
```

```

System.bool InterlockSurface {get; set;}
```

```

property System.bool InterlockSurface {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to create an interlock surface, false to not

Remarks

If this property is set to true, then you can specify a [draft angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~Angle.md) for the interlock surface.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md)  
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.md)
