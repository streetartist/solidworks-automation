# Clockwise Property (IHelixFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Clockwise`

Gets or sets the direction of the turns of this helix feature.
Gets or sets the direction of the turns of this helix feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Clockwise As System.Boolean
```

```

Dim instance As IHelixFeatureData
Dim value As System.Boolean
 
instance.Clockwise = value
 
value = instance.Clockwise
```

```

System.bool Clockwise {get; set;}
```

```

property System.bool Clockwise {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if direction of turns is clockwise, false if  counterclockwise

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md)  
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.md)
