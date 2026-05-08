# TargetStyle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TargetStyle`

Gets or sets the type of connection at the target point for this callout.
Gets or sets the type of connection at the target point for this callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TargetStyle As System.Integer
```

```

Dim instance As ICallout
Dim value As System.Integer
 
instance.TargetStyle = value
 
value = instance.TargetStyle
```

```

System.int TargetStyle {get; set;}
```

```

property System.int TargetStyle {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Connection style as defined in [swCalloutTargetStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCalloutTargetStyle_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)
