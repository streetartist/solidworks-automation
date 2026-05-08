# GetAnnotation Method (IDatumOrigin)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetAnnotation`

Gets the IAnnotation object for this datum origin.
Gets the [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object for this datum origin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAnnotation() As Annotation
```

```

Dim instance As IDatumOrigin
Dim value As Annotation
 
value = instance.GetAnnotation()
```

```

Annotation GetAnnotation()
```

```

Annotation^ GetAnnotation(); 
```

#### Return Value

Pointer to the [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object for this annotation

Remarks

The IAnnotation object is a higher-level object that contains methods that apply to all types of annotations.

Example

[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)  
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)  
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md)  
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.md)
