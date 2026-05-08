# Direction Property (IShellFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~Direction`

Gets and sets the direction of this shell feature.
Gets and sets the direction of this shell feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Direction As System.Integer
```

```

Dim instance As IShellFeatureData
Dim value As System.Integer
 
instance.Direction = value
 
value = instance.Direction
```

```

System.int Direction {get; set;}
```

```

property System.int Direction {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

0 for inward shell, 1 for outward shell

Example

See the [IShellFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.md)  
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.md)
