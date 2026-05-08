# PasteAppearance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PasteAppearance`

Applies to the specified entity an appearance that has been copied to the clipboard.
Applies to the specified entity an appearance that has been copied to the clipboard.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PasteAppearance( _
   ByVal Object As System.Object, _
   ByVal AppearanceTarget As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Object As System.Object
Dim AppearanceTarget As System.Integer
Dim value As System.Boolean
 
value = instance.PasteAppearance(Object, AppearanceTarget)
```

```

System.bool PasteAppearance( 
   System.object Object,
   System.int AppearanceTarget
)
```

```

System.bool PasteAppearance( 
   System.Object^ Object,
   System.int AppearanceTarget
) 
```

#### Parameters

*Object*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md), [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md), [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md), or [part](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) to which to apply a copied appearance; if Null, the copied appearance is applied to an entity that is pre-selected in the graphics area

*AppearanceTarget*
:   Appearance target type as defined in [swAppearanceTargetType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppearanceTargetType_e.html); only valid if Object is a face

#### Return Value

True if the copied appearance is successfully applied, false if not

Example

[Copy and Paste Appearances (VBA)](Copy_and_Paste_Appearances_Example_VB.htm)  
[Copy and Paste Appearances (VB.NET)](Copy_and_Paste_Appearances_Example_VBNET.htm)  
[Copy and Paste Appearances (C#)](Copy_and_Paste_Appearances_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::CopyAppearance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyAppearance.md)
