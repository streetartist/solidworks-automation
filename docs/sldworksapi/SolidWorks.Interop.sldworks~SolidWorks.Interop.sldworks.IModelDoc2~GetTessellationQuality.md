# GetTessellationQuality Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetTessellationQuality`

Gets the shaded-display image quality number for the current document.
Gets the shaded-display image quality number for the current document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTessellationQuality() As System.Integer
```

```

Dim instance As IModelDoc2
Dim value As System.Integer
 
value = instance.GetTessellationQuality()
```

```

System.int GetTessellationQuality()
```

```

System.int GetTessellationQuality(); 
```

#### Return Value

0 < Shaded-display image quality number < 106 (see **Remarks**)

Remarks

This method returns a number (*QualityNum*) that corresponds to the degree of tessellation of curved surfaces for shaded rendering output. **Tools > Options > Document Properties > Image Quality** includes a field that sets the maximum chordal deviation. *QualityNum* and the maximum chordal deviation (in meters) are coupled and inversely proportional as follows:

*var* = *TessMin* + *QualityNum*\*((*TessMax*-*TessMin*)/100)

*Deviation* = 0.025 \* (*BodyDiameter* \* 2) / *var*;

where:

- *TessMin* = 6
- *TessMax* = 166
- 0 < *QualityNum* (returned by this method) < 106
- *BodyDiameter* is the diagonal distance across the bounds of the part box. See [IPartDoc::GetPartBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetPartBox.md) or [IPartDoc::IGetPartBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetPartBox.md) for more information.

You can also get the maximum chordal deviation using [swUserPreferencesDouble\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceDoubleValue_e.html).swImageQualityShadedDeviation.

To get the image quality number, use [swUserPreferenceInteger\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.html).swImageQualityShaded.

**NOTE:** [Setting the degree of tessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetTessellationQuality.md) to a higher value results in:

- finer tessellation,
- increased file size,
- slower graphics performance, and
- increased memory usage.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
