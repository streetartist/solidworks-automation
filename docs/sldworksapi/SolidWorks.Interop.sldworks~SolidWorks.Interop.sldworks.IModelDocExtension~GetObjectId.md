# GetObjectId Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectId`

Gets the object ID for the specified annotation.
Gets the object ID for the specified annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetObjectId( _
   ByVal Annotation As Annotation _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim Annotation As Annotation
Dim value As System.Integer
 
value = instance.GetObjectId(Annotation)
```

```

System.int GetObjectId( 
   Annotation Annotation
)
```

```

System.int GetObjectId( 
   Annotation^ Annotation
) 
```

#### Parameters

*Annotation*
:   [Annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

#### Return Value

Object ID

Example

[Get Object ID of GTol Annotation (C#)](Get_Object_ID_of_GTol_Annotation_Example_CSharp.htm)  
[Get Object ID of GTol Annotation (VB.NET)](Get_Object_ID_of_GTol_Annotation_Example_VBNET.htm)  
[Get Object ID of GTol Annotation (VBA)](Get_Object_ID_of_GTol_Annotation_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
