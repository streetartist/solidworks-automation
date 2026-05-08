# AddComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents`

Obsolete. Superseded by IAssemblyDoc::AddComponents3.
Obsolete. Superseded by [IAssemblyDoc::AddComponents3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddComponents( _
   ByVal Names As System.Object, _
   ByVal Transforms As System.Object _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim Names As System.Object
Dim Transforms As System.Object
Dim value As System.Object
 
value = instance.AddComponents(Names, Transforms)
```

```

System.object AddComponents( 
   System.object Names,
   System.object Transforms
)
```

```

System.Object^ AddComponents( 
   System.Object^ Names,
   System.Object^ Transforms
) 
```

#### Parameters

*Names*
:   Array of strings component file names

*Transforms*
:   Array of doubles of the component transforms

#### Return Value

Array of objects of newly created components

Remarks

The array of file names represents all of the components that are added to the assembly. If there is more than one instance of a given component, make sure you add the file name of the component for each instance of the component.

The array of transforms consists of [count x 16] doubles. There should be one transform for each component being added.

**TIP**: See [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) for tips on how to avoid using large amounts of memory when opening up multiple parts to add to an assembly

Example

[Add Components (VBA)](Add_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::IAddComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents2.md)
