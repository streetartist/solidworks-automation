# Depth Property (IToolingSplitFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~Depth`

Gets or sets the depth of the block in the specified direction for this tooling split feature.
Gets or sets the depth of the block in the specified direction for this tooling split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Depth( _
   ByVal Dir As System.Integer _
) As System.Double
```

```

Dim instance As IToolingSplitFeatureData
Dim Dir As System.Integer
Dim value As System.Double
 
instance.Depth(Dir) = value
 
value = instance.Depth(Dir)
```

```

System.double Depth( 
   System.int Dir
) {get; set;}
```

```

property System.double Depth {
   System.double get(System.int Dir);
   void set (System.int Dir, System.double value);
}
```

#### Parameters

*Dir*
:   - 0 = Depth in Direction 1
    - 1 = Depth in Direction 2

#### Property Value

Depth

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md)  
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.md)
