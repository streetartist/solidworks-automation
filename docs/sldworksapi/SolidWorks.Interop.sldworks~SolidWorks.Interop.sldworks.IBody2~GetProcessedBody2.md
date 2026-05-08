# GetProcessedBody2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2`

Pre-processes the geometry of the body using the specified parameters.
Pre-processes the geometry of the body using the specified parameters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetProcessedBody2( _
   ByVal MaxUAngle As System.Double, _
   ByVal MaxVAngle As System.Double _
) As Body2
```

```

Dim instance As IBody2
Dim MaxUAngle As System.Double
Dim MaxVAngle As System.Double
Dim value As Body2
 
value = instance.GetProcessedBody2(MaxUAngle, MaxVAngle)
```

```

Body2 GetProcessedBody2( 
   System.double MaxUAngle,
   System.double MaxVAngle
)
```

```

Body2^ GetProcessedBody2( 
   System.double MaxUAngle,
   System.double MaxVAngle
) 
```

#### Parameters

*MaxUAngle*
:   Maximum U angle

*MaxVAngle*
:   Maximum V angle

#### Return Value

Pointer to the [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md); this body is a processed copy of the body for this part

Remarks

Pre-processing (for example, IGES) is sometimes necessary for exporting to systems that have difficulty with periodic conditions.

Faces that lie on periodic surfaces that are not closed in the periodic direction might have bounds returned by [IFace2::GetUVBounds](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetUVBounds.md) that are on the periodic seam. Use [IModeler::SplitFaceOnParam](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SplitFaceOnParam.md) if the application needs to ensure that the face bounds lie completely on the surface bounds.

This method does not split at a seam unless the face is closed in that parameter. Splitting only occurs if the face has a parametric extent greater than the specified pitch.

Example

[Process Body (C#)](Process_Body_Example_CSharp.htm)  
[Process Body (VB.NET)](Process_Body_Example_VBNET.htm)  
[Process Body (VBA)](Process_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IGetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.md)  
[IBody2::GetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.md)  
[IPartDoc::IGetProcessedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetProcessedBody2.md)
