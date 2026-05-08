# SaveIsolate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SaveIsolate`

Saves the display characteristics of the isolated components to a new display state.
Saves the display characteristics of the [isolated components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~Isolate.md) to a new display state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveIsolate( _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.SaveIsolate(Name)
```

```

System.bool SaveIsolate( 
   System.string Name
)
```

```

System.bool SaveIsolate( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of the new display state to which to save the characteristics of the isolated components

#### Return Value

True if a new display state of the characteristics of the isolated components is created, false if not

Example

[Isolate Component (C#)](Isolate_Component_Example_CSharp.htm)  
[Isolate Component (VB.NET)](Isolate_Component_Example_VBNET.htm)  
[Isolate Component (VBA)](Isolate_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::ExitIsolate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ExitIsolate.md)  
[IAssemblyDoc::SetIsolateVisibility Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetIsolateVisibility.md)
