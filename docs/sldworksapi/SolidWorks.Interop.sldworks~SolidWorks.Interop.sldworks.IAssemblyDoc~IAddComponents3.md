# IAddComponents3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents3`

Adds multiple components to the assembly.
Adds multiple components to the assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddComponents3( _
   ByVal Count As System.Integer, _
   ByRef Names As System.String, _
   ByRef Transforms As System.Double, _
   ByVal CoordinateSystemNameCount As System.Integer, _
   ByRef CoordinateSystemNames As System.String _
) As Component2
```

```

Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim Names As System.String
Dim Transforms As System.Double
Dim CoordinateSystemNameCount As System.Integer
Dim CoordinateSystemNames As System.String
Dim value As Component2
 
value = instance.IAddComponents3(Count, Names, Transforms, CoordinateSystemNameCount, CoordinateSystemNames)
```

```

Component2 IAddComponents3( 
   System.int Count,
   ref System.string Names,
   ref System.double Transforms,
   System.int CoordinateSystemNameCount,
   ref System.string CoordinateSystemNames
)
```

```

Component2^ IAddComponents3( 
   System.int Count,
   System.String^% Names,
   System.double% Transforms,
   System.int CoordinateSystemNameCount,
   System.String^% CoordinateSystemNames
) 
```

#### Parameters

*Count*
:   Number of components to add

*Names*
:   - in-process, unmanaged C++: Pointer to an array of strings of full path names of components to add

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*Transforms*
:   - in-process, unmanaged C++: Pointer to an array of doubles of component transforms

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*CoordinateSystemNameCount*
:   Number of coordinate system names in CoordinateSystemNames; include in the count all empty strings

*CoordinateSystemNames*
:   - in-process, unmanaged C++: Pointer to an array of strings of coordinate system names

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Transforms contains an array of [Count x 16] doubles. This parameter stores one transformation matrix of 16 doubles for each component in Names. If a component's transformation matrix is null, then the component is placed in the assembly such that the component's user-defined coordinate system coincides exactly with the default coordinate system of the assembly (no transformation). See [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) for details about transformation matrices.

CoordinateSystemNames contains a user-defined coordinate system name for each component in Names. If a component's user-defined coordinate system is an empty string, then the component is placed in the assembly with respect to the default coordinate system of the component.

The application must allocate the array of components, and it is also responsible for releasing the returned array of components.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AddComponents3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents3.md)
