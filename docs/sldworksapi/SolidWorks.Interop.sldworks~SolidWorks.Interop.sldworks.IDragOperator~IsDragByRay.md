# IsDragByRay Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IsDragByRay`

Gets or sets the drag-by-ray setting.
Gets or sets the drag-by-ray setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IsDragByRay As System.Boolean
```

```

Dim instance As IDragOperator
Dim value As System.Boolean
 
instance.IsDragByRay = value
 
value = instance.IsDragByRay
```

```

System.bool IsDragByRay {get; set;}
```

```

property System.bool IsDragByRay {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True uses drag-by-ray, false uses drag-by-transform (see **Remarks**)

Remarks

- Drag-by-ray Tries to find a solution that keeps a specified geometry on, or close to, a ray (defined by a point on the ray and its direction).
- Drag-by-transform Uses a transform matrix, which is any combination of translations and rotations.

NOTE: IDragOperator does not define the drag ray; it only performs drag-by-transform. If this property is set to True, the user-interface component move honors this setting. The default mode for the user interface is drag-by-transform.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)
