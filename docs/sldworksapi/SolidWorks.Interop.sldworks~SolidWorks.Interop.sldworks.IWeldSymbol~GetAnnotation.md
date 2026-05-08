# GetAnnotation Method (IWeldSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetAnnotation`

Gets the annotation for this weld symbol.
Gets the annotation for this weld symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAnnotation() As System.Object
```

```

Dim instance As IWeldSymbol
Dim value As System.Object
 
value = instance.GetAnnotation()
```

```

System.object GetAnnotation()
```

```

System.Object^ GetAnnotation(); 
```

#### Return Value

[Annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

Remarks

This method obtains the owning [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object, which is a higher-level object that contains methods that are general to all types of annotations.

Example

[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)  
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)  
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)  
[IWeldSymbol::IGetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetAnnotation.md)
