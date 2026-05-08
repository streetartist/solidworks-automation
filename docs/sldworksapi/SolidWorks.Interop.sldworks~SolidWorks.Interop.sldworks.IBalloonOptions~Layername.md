# Layername Property (IBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~Layername`

Gets and sets the name of the layer on which to create the balloon.
Gets and sets the name of the layer on which to create the balloon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Layername As System.String
```

```

Dim instance As IBalloonOptions
Dim value As System.String
 
instance.Layername = value
 
value = instance.Layername
```

```

System.string Layername {get; set;}
```

```

property System.String^ Layername {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Layer name

Remarks

See the SOLIDWORKS Help for additional details about balloons.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md)  
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.md)
