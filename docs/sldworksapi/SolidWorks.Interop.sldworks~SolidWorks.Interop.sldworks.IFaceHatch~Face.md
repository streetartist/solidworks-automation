# Face Property (IFaceHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~Face`

Gets the face that is associated with the hatch.
Gets the face that is associated with the hatch.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Face As Face2
```

```

Dim instance As IFaceHatch
Dim value As Face2
 
instance.Face = value
 
value = instance.Face
```

```

Face2 Face {get; set;}
```

```

property Face2^ Face {
   Face2^ get();
   void set (    Face2^ value);
}
```

#### Property Value

Pointer to the [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) associated with the hatch

Example

[Get Hatching Data (VBA)](Get_Hatching_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.md)  
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.md)
