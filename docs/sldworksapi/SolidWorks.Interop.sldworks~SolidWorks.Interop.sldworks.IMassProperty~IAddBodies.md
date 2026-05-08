# IAddBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IAddBodies`

Uses only the specified bodies when calculating the mass properties for this model.
Uses only the specified bodies when calculating the mass properties for this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddBodies( _
   ByVal NumBodies As System.Integer, _
   ByRef BodyListIn As Body2 _
) As System.Boolean
```

```

Dim instance As IMassProperty
Dim NumBodies As System.Integer
Dim BodyListIn As Body2
Dim value As System.Boolean
 
value = instance.IAddBodies(NumBodies, BodyListIn)
```

```

System.bool IAddBodies( 
   System.int NumBodies,
   ref Body2 BodyListIn
)
```

```

System.bool IAddBodies( 
   System.int NumBodies,
   Body2^% BodyListIn
) 
```

#### Parameters

*NumBodies*
:   Number of bodies in the model

*BodyListIn*
:   - in-process, unmanaged C++: Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) in the model of size NumBodies

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if the specified bodies are used for calculating mass properties, false if not

Remarks

This method lets you select which solid bodies to use when calculating mass properties, much like a end-user selecting the bodies via the interface.

NOTE: If a sheet (surface) body is specified, it is ignored and false is returned.

The results of the mass property calculations vary based on whether or not this method is used.  

|  |  |
| --- | --- |
| **If this method is...** | **Then...** |
| Called and bodies are specified | These bodies can either be from a subset of the documents body list or from temporary bodies.    NOTE: Each specified body should either come from the owning document or be a temporary body. If the body does not satisfy either case, then it is not used when calculating the mass properties. |
| Not called | Mass properties' calculations include all available bodies in the document.   - Part. All of the solid bodies are included in the calculations. - Assembly. All of the bodies in all of the components are used in the calculations. |

If the document from which the MassProperty object came is an assembly, then any body from any of the child components can be used. To obtain the body, call [IComponent2::GetBodies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies2.md). Your application does not need to make a copy of the body or apply a transform to the body.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IMassProperty::AddBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~AddBodies.md)
