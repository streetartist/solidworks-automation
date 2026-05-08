# Mates Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~Mates`

Gets or sets the mates in this mate controller.
Gets or sets the mates in this mate controller.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Mates As System.Object
```

```

Dim instance As IMateControllerFeatureData
Dim value As System.Object
 
instance.Mates = value
 
value = instance.Mates
```

```

System.object Mates {get; set;}
```

```

property System.Object^ Mates {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of supportive [mates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)

Remarks

This property is only valid after the mate controller is created.

To create a mate controller see the Remarks section of IMateControllerFeatureData.

Example

See the [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md)  
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.md)
