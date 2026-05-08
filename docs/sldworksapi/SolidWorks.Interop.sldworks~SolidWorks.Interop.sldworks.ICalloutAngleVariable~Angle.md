# Angle Property (ICalloutAngleVariable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable~Angle`

Gets the value of an angle variable in a hole callout.
Gets the value of an angle variable in a hole callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Angle As System.Double
```

```

Dim instance As ICalloutAngleVariable
Dim value As System.Double
 
value = instance.Angle
```

```

System.double Angle {get;}
```

```

property System.double Angle {
   System.double get();
}
```

#### Property Value

Angle in radians

Example

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)  
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)  
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICalloutAngleVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable.md)  
[ICalloutAngleVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable_members.md)  
[ICalloutAngleVariable::Precision Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable~Precision.md)
