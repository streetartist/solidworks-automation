# IAddComponents2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents2`

Obsolete. Superseded by IAssemblyDoc::IAddComponents3.
Obsolete. Superseded by [IAssemblyDoc::IAddComponents3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddComponents2( _
   ByRef Count As System.Integer, _
   ByRef Names As System.String, _
   ByRef Transforms As System.Double _
) As Component2
```

```

Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim Names As System.String
Dim Transforms As System.Double
Dim value As Component2
 
value = instance.IAddComponents2(Count, Names, Transforms)
```

```

Component2 IAddComponents2( 
   ref System.int Count,
   ref System.string Names,
   ref System.double Transforms
)
```

```

Component2^ IAddComponents2( 
   System.int% Count,
   System.String^% Names,
   System.double% Transforms
) 
```

#### Parameters

*Count*
:   Number of components to add

*Names*
:   - in-process, unmanaged C++: Pointer to an array of strings of component file names

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*Transforms*
:   - in-process, unmanaged C++: Pointer to an array of doubles of component transforms

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The array of file names represents all of the components that you want to add to the assembly. If there is more than one instance of a given component, make sure to specify the file name for each instance of the component that you want to add.

The array of transforms consists of [count x 16] doubles. There should be one transform for each component to be added.

The application must allocate the array of components, and it is also responsible for releasing the returned array of components.

Example

[Add Components and Transforms (C++)](Add_Components_and_Transforms_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AddComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents.md)
