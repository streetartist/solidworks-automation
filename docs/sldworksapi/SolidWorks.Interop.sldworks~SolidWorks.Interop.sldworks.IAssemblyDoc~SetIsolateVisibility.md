# SetIsolateVisibility Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetIsolateVisibility`

Sets the display characteristics of all of the components not selected to isolate.
Sets the display characteristics of all of the components not selected to [isolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~Isolate.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetIsolateVisibility( _
   ByVal Option As System.Integer _
) 
```

```

Dim instance As IAssemblyDoc
Dim Option As System.Integer
 
instance.SetIsolateVisibility(Option)
```

```

void SetIsolateVisibility( 
   System.int Option
)
```

```

void SetIsolateVisibility( 
   System.int Option
) 
```

#### Parameters

*Option*
:   Display characteristics of all of the components not selected to isolate as defined in [swIsolateVisibility\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swIsolateVisibility_e.html)

Remarks

Before you [exit isolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ExitIsolate.md), you can [save the display characteristics to a new display state](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SaveIsolate.md), which you can access from the ConfigurationManager. If you do not save before exiting isolate, then the display returns to its original state.

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
