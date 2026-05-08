# IAddProfileBsplineDLL Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileBsplineDLL`

Obsolete. Superseded by IBody2::IAddProfileBsplineDLL.
Obsolete. Superseded by [IBody2::IAddProfileBsplineDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBsplineDLL.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddProfileBsplineDLL( _
   ByRef Properties As System.Integer, _
   ByRef KnotArray As System.Double, _
   ByRef ControlPointCoordArray As System.Double _
) As Curve
```

```

Dim instance As IBody
Dim Properties As System.Integer
Dim KnotArray As System.Double
Dim ControlPointCoordArray As System.Double
Dim value As Curve
 
value = instance.IAddProfileBsplineDLL(Properties, KnotArray, ControlPointCoordArray)
```

```

Curve IAddProfileBsplineDLL( 
   ref System.int Properties,
   ref System.double KnotArray,
   ref System.double ControlPointCoordArray
)
```

```

Curve^ IAddProfileBsplineDLL( 
   System.int% Properties,
   System.double% KnotArray,
   System.double% ControlPointCoordArray
) 
```

#### Parameters

*Properties*

*KnotArray*

*ControlPointCoordArray*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
