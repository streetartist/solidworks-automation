# ToleranceType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceType`

Gets or sets the type of tolerance for a hole callout.
Gets or sets the type of tolerance for a hole callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ToleranceType As System.Integer
```

```

Dim instance As ICalloutVariable
Dim value As System.Integer
 
instance.ToleranceType = value
 
value = instance.ToleranceType
```

```

System.int ToleranceType {get; set;}
```

```

property System.int ToleranceType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of tolerance as defined in [swTolType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html) (see **Remarks**)

Remarks

In SOLIDWORKS 2016 and later, use this property to set the type of tolerance for a hole callout. Calling [IDimensionTolerance::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.md) to set the type of tolerance for a hole callout does not override this property's setting.

To see the effects of changing the tolerance type, use [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md).

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
