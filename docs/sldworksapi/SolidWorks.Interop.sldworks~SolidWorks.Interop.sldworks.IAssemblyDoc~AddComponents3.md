# AddComponents3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents3`

Adds multiple components to the assembly.
Adds multiple components to the assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddComponents3( _
   ByVal Names As System.Object, _
   ByVal Transforms As System.Object, _
   ByVal CoordinateSystemNames As System.Object _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim Names As System.Object
Dim Transforms As System.Object
Dim CoordinateSystemNames As System.Object
Dim value As System.Object
 
value = instance.AddComponents3(Names, Transforms, CoordinateSystemNames)
```

```

System.object AddComponents3( 
   System.object Names,
   System.object Transforms,
   System.object CoordinateSystemNames
)
```

```

System.Object^ AddComponents3( 
   System.Object^ Names,
   System.Object^ Transforms,
   System.Object^ CoordinateSystemNames
) 
```

#### Parameters

*Names*
:   Array of full path names of components

*Transforms*
:   Array of transformation matrix doubles

*CoordinateSystemNames*
:   Array of coordinate system names

#### Return Value

Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) objects

Remarks

Transforms contains an array of [(Names count) x 16] doubles. This parameter stores one transformation matrix of 16 doubles for each component in Names. If a component's transformation matrix is null, then the component is placed in the assembly such that the component's user-defined coordinate system coincides exactly with the default coordinate system of the assembly (no transformation). See [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) for details about transformation matrices.

CoordinateSystemNames contains a user-defined coordinate system name for each component in Names. If a component's user-defined coordinate system is an empty string, then the component is placed in the assembly with respect to the default coordinate system of the component.

**TIP**: See [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) for tips on how to avoid using large amounts of memory when opening up multiple parts to add to an assembly

Example

[Add Components (C#)](Add_Components_Example_CSharp.htm)  
[Add Components (VB.NET)](Add_Components_Example_VBNET.htm)  
[Add Components (VBA)](Add_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::IAddComponents3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents3.md)
