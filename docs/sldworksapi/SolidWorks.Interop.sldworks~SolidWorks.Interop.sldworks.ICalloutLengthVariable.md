# ICalloutLengthVariable Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable`

Allows access to a length variable in a hole callout.
Allows access to a length variable in a hole callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICalloutLengthVariable 
```

```

Dim instance As ICalloutLengthVariable
```

```

public interface ICalloutLengthVariable 
```

```

public interface class ICalloutLengthVariable 
```

Remarks

To access a CalloutLengthVariable object:

1. Call [IDisplayDimension::GetHoleCalloutVariables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetHoleCalloutVariables.md).
2. Iterate through the [CalloutVariable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.md) objects returned by IDisplayDimension::GetHoleCalloutVariables and call [ICalloutVariable::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~Type.md).

If the type of hole callout equals [swCalloutVariableType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCalloutVariableType_e.html).swCalloutVariable\_Length, then that object is a CalloutLengthVariable object.

Example

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)  
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)  
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICalloutLengthVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ICalloutAngleVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable.md)  
[ICalloutStringVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutStringVariable.md)
