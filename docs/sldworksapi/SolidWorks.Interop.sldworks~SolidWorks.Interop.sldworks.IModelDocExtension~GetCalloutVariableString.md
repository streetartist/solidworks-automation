# GetCalloutVariableString Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCalloutVariableString`

Gets the string for the specified callout variable.
Gets the string for the specified callout variable.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCalloutVariableString( _
   ByVal Variable As System.Integer _
) As System.String
```

```

Dim instance As IModelDocExtension
Dim Variable As System.Integer
Dim value As System.String
 
value = instance.GetCalloutVariableString(Variable)
```

```

System.string GetCalloutVariableString( 
   System.int Variable
)
```

```

System.String^ GetCalloutVariableString( 
   System.int Variable
) 
```

#### Parameters

*Variable*
:   Callout variable as defined in [swCalloutVariable\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCalloutVariable_e.html)

#### Return Value

Callout variable string

Example

[Create Advanced Hole (VBA)](Create_Advanced_Hole_Example_VB.htm)  
[Create Advanced Hole (VB.NET)](Create_Advanced_Hole_Example_VBNET.htm)  
[Create Advanced Hole (C#)](Create_Advanced_Hole_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IAdvancedHoleElementData::CalloutString Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~CalloutString.md)
