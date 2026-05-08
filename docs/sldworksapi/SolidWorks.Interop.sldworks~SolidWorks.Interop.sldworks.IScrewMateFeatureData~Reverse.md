# Reverse Property (IScrewMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~Reverse`

Gets or sets whether to change the direction of movement of the components relative to one another.
Gets or sets whether to change the direction of movement of the components relative to one another.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Reverse As System.Boolean
```

```

Dim instance As IScrewMateFeatureData
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

True to reverse the direction of movement of the components, false to not

Example

See the [IScrewMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IScrewMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.md)  
[IScrewMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData_members.md)
