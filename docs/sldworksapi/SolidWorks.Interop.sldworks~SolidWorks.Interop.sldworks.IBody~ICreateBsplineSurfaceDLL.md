# ICreateBsplineSurfaceDLL Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateBsplineSurfaceDLL`

Obsolete. Superseded by IBody2::ICreateBsplineSurfaceDLL.
Obsolete. Superseded by [IBody2::ICreateBsplineSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBsplineSurfaceDLL.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBsplineSurfaceDLL( _
   ByRef Properties As System.Integer, _
   ByRef UKnotArray As System.Double, _
   ByRef VKnotArray As System.Double, _
   ByRef ControlPointCoordArray As System.Double _
) As Surface
```

```

Dim instance As IBody
Dim Properties As System.Integer
Dim UKnotArray As System.Double
Dim VKnotArray As System.Double
Dim ControlPointCoordArray As System.Double
Dim value As Surface
 
value = instance.ICreateBsplineSurfaceDLL(Properties, UKnotArray, VKnotArray, ControlPointCoordArray)
```

```

Surface ICreateBsplineSurfaceDLL( 
   ref System.int Properties,
   ref System.double UKnotArray,
   ref System.double VKnotArray,
   ref System.double ControlPointCoordArray
)
```

```

Surface^ ICreateBsplineSurfaceDLL( 
   System.int% Properties,
   System.double% UKnotArray,
   System.double% VKnotArray,
   System.double% ControlPointCoordArray
) 
```

#### Parameters

*Properties*

*UKnotArray*

*VKnotArray*

*ControlPointCoordArray*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
