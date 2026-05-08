# GetTessTriangles Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessTriangles`

Gets the triangles that make up the shaded picture tessellation for this component.
Gets the triangles that make up the shaded picture tessellation for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTessTriangles( _
   ByVal NoConversion As System.Boolean _
) As System.Object
```

```

Dim instance As IComponent2
Dim NoConversion As System.Boolean
Dim value As System.Object
 
value = instance.GetTessTriangles(NoConversion)
```

```

System.object GetTessTriangles( 
   System.bool NoConversion
)
```

```

System.Object^ GetTessTriangles( 
   System.bool NoConversion
) 
```

#### Parameters

*NoConversion*
:   True prohibits conversion to user units from system units, false does not

#### Return Value

Array (see **Remarks**)

Remarks

Tessellation information is available only when the component is loaded as lightweight.

These triangles are intended for graphics display purposes and do not represent a tessellation that could be used, for example, by a machining application. If you need the type of accuracy associated with a machining product, we recommend that you traverse the body faces and extract the topology and geometry data to create your own faceting.

The format of the returned data is:

- float x, y, z - first point in meters
- float x, y, z - second point in meters
- float x, y, z - third point in meters

for the set of triangles for the component.

The total size of the data is [ 9 x sizeof(float) x (number of triangles) ].

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::IGetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriangles.md)
