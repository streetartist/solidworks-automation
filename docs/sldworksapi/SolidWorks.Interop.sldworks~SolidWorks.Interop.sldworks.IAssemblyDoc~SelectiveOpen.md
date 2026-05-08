# SelectiveOpen Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen`

Selectively opens the components of an assembly that is opened in Large Design Review mode.
Selectively opens the components of an assembly that is opened in Large Design Review mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectiveOpen( _
   ByVal SelectedComponents As System.Boolean, _
   ByVal OpenLightWeight As System.Boolean _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim SelectedComponents As System.Boolean
Dim OpenLightWeight As System.Boolean
Dim value As System.Boolean
 
value = instance.SelectiveOpen(SelectedComponents, OpenLightWeight)
```

```

System.bool SelectiveOpen( 
   System.bool SelectedComponents,
   System.bool OpenLightWeight
)
```

```

System.bool SelectiveOpen( 
   System.bool SelectedComponents,
   System.bool OpenLightWeight
) 
```

#### Parameters

*SelectedComponents*
:   True to open only the components in the current selection list, false to open all of the components in the assembly

*OpenLightWeight*
:   True to open the components in lightweight mode, false to not

#### Return Value

True if successful, false if not (see **Remarks**)

Remarks

This method only works for assemblies that are opened in Large Design Review mode.

To open an assembly in Large Design Review mode:

1. Call [ISldWorks::GetOpenDocSpec](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocSpec.md) to create an instance of [IDocumentSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md).
2. Set [IDocumentSpecification::ViewOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ViewOnly.md) to true.
3. Call [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md), passing it the instance of IDocumentSpecification.

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the components that you want to open.

Example

[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)  
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)  
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[ISldWorks::OpenDoc6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md)  
[IAssemblyDoc::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.md)  
[IAssemblyDoc::GetLightWeightComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetLightWeightComponentCount.md)  
[IAssemblyDoc::MakeLightWeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MakeLightWeight.md)  
[IAssemblyDoc::ResolveAllLightweight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightweight.md)  
[IAssemblyDoc::ResolveAllLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.md)  
[IAssemblyDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.md)
