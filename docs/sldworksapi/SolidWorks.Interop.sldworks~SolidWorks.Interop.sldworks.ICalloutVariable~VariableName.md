# VariableName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~VariableName`

Gets the name of the hole callout variable as it appears in the Dimension PropertyManager page in the Dimension Text box.
Gets the name of the hole callout variable as it appears in the Dimension PropertyManager page in the **Dimension Text** box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property VariableName As System.String
```

```

Dim instance As ICalloutVariable
Dim value As System.String
 
value = instance.VariableName
```

```

System.string VariableName {get;}
```

```

property System.String^ VariableName {
   System.String^ get();
}
```

#### Property Value

Name of the hole callout variable as it appears in the Dimension PropertyManager page in the **Dimension Text** box

Remarks

Call [ICalloutVariable::UserReadableVariableName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~UserReadableVariableName.md) to get the name of the hole callout variable as it appears in the Dimension PropertyManager page in the **Callout value** drop-down list box.

Example

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)  
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)  
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.md)  
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.md)
